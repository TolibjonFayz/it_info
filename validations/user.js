const joi = require("joi");

exports.userValidation = (data) => {
  const schema = joi.object({
    user_name: joi.string().pattern(new RegExp("^[a-zA-Z]{2,50}$")).required(),
    user_email: joi.string().required().email(),
    user_password: joi.string().min(6).max(20).required(),
    user_is_active: joi.boolean().required(),
    user_is_creator: joi.boolean().required(),
    created_data: joi.string().required(),
    updated_at: joi.string().required()
  });
  return schema.validate(data, { abortEarly: false });
};
