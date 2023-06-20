const joi = require("joi");

const authorSchema = joi.object({
  author_first_name: joi
    .string()
    .pattern(new RegExp("^[a-zA-Z]{2,50}$"))
    .required(),
  author_last_name: joi
    .string()
    .pattern(new RegExp("^[a-zA-Z]{2,50}$"))
    .required(),
  author_nick_name: joi.string().max(20),
  author_password: joi.string().min(6).max(20),
  confirm_password: joi.ref("author_password"),
  author_email: joi.string().email(),
  author_phone: joi.string().pattern(/\d{2}-\d{3}-\d{2}-\d{2}/),
  author_info: joi.string(),
  author_position: joi.string(),
  author_photo: joi.string().default("/author/avatar.jpg"),
  is_expert: joi.boolean().default(false),
});

module.exports = authorSchema;
