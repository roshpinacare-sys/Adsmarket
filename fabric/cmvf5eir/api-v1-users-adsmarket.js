const jwt = require('jsonwebtoken');
const User = require('../models/User');

// Middleware for JWT authentication
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// Middleware for RBAC authorization
const authorizeRole = (...allowedRoles) => {
  return (req, res, next) => {
    if (!req.user) return res.sendStatus(401);
    if (!allowedRoles.includes(req.user.role)) {
      return res.sendStatus(403);
    }
    next();
  };
};

// GET /api/v1/users - List users (admin only)
const getUsers = [
  authenticateToken,
  authorizeRole('admin'),
  async (req, res) => {
    try {
      const users = await User.find({}, '-password');
      res.json(users);
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  }
];

// PUT /api/v1/users/:id - Update user (admin or self)
const updateUser = [
  authenticateToken,
  authorizeRole('admin', 'user'),
  async (req, res) => {
    try {
      const user = await User.findById(req.params.id);
      if (!user) return res.sendStatus(404);

      // Ownership check: user can only update themselves unless admin
      if (req.user.role !== 'admin' && req.user.id !== user.id.toString()) {
        return res.sendStatus(403);
      }

      Object.assign(user, req.body);
      await user.save();
      res.json({ id: user.id, name: user.name, email: user.email, role: user.role });
    } catch (err) {
      res.status(400).json({ message: err.message });
    }
  }
];

module.exports = { getUsers, updateUser };