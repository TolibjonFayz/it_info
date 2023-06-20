const joi = require("joi");

const authorEmailPassSchema = joi.object({
  author_email: joi.string().email().message("Invalid email").required(),
  author_password: joi.string().min(6).max(30).required(),
});

module.exports = authorEmailPassSchema;
