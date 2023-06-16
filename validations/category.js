const joi = require("joi");

exports.categoryvalidation = (data) => {
  const schema = joi.object({
    category_name: joi
      .string()
      .min(2)
      .message("Kategoriya nomi 2ta harfadn koproq bolishi kerak!")
      .max(255)
      .message("Kaegoriya nomi 255ta harfdan uzun bo'lmasligi kerak!"),
    parent_category_id: joi.string().alphanum(),
  });
  return schema.validate(data);
};
