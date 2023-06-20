const joi = require("joi");

const adminSchema = joi.object({
  admin_name: joi.string().pattern(new RegExp("^[a-zA-Z]{2,50}$")).required(),
  admin_email: joi.string().email().required(),
  admin_password: joi.string().min(6).max(20),
  admin_is_active: joi.boolean().default(true),
  admin_is_creator: joi.boolean().default(false),
  created_data: joi.string().required(),
  updated_at: joi.string(),
});

module.exports = adminSchema;
