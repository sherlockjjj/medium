const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const mongoose = require("mongoose");
const Topic = require('./models/topic');

const articleSchema = mongoose.Schema({
  _id: { type: String, required: true },
  tag: { type: String, required: true },
  title: { type: String, required: true },
  author: { type: String, required: true },
  publish_time: Date,
  url: String,
  author_url: String,
  headings: String,
  contents: String,
  min_read: String,
  lang: String,
  claps: Number
});

mongoose
  .connect(
    "mongodb://localhost:27017/mediumPosts"
  )
  .then(() => {
    console.log("Connected to database!");
  })
  .catch(() => {
    console.log("Connection failed!");
  });

app.use(bodyParser.json());

app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept");
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, PATCH, DELETE, OPTIONS")
  next();
});

app.get("/api/topics", (req, res, next) => {
  Topic.find().then(documents => {
    res.status(200).json({
      topics: documents
    });
  });
});

app.get("/api/articles/:topic", (req, res, next) => {
  const topic = req.params.topic;
  const Article = mongoose.model(topic, articleSchema, topic);

  Article.find().limit(20).then(documents => {
    res.status(200).json({
      articles: documents
    });
  });
});
module.exports = app;
