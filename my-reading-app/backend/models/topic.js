const mongoose = require('mongoose');

const topicSchema = mongoose.Schema(
  {
    _id: { type: String, required: true },
    name: { type: String, required: true }
  },
);

module.exports = mongoose.model('topics', topicSchema);
