const joi = require("joi");

const adminEmailPassSchema = joi.object({
  admin_email: joi.string().email().message("Invalid email").required(),
  admin_password: joi.string().min(6).max(30).required(),
});
module.exports = adminEmailPassSchema;
