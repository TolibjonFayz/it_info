const joi = require("joi");

exports.userValidation = (data) => {
  const schema = joi.object({
    user_name: joi.string().pattern("^[a-zA-Z]{2,50}$").required(),
    user_email: joi.string().required().email(),
    user_password: joi.string().min(6).max(20).required(),
  });
};
