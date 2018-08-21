const mongoose = require('mongoose');

const articleSchema = mongoose.Schema({
  id: { type: String, required: true },
  tag: { type: String, required: true },
  title: { type: String, required: true },
  author: { type: String, required: true },
});

module.exports = mongoose.model('article', articleSchema);
