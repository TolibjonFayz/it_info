const Validators = require("../validations");

module.exports = function (validator) {
  if (!Validators.hasOwnProperty(validator))
    throw new Error(`'${validator}' validator is not exist`);

  return async function (req, res, next) {
    try {
      const validated = await Validators[validator].validateAsync(req.body);
      req.body = validated;
      next();
    } catch (err) {
      if (err.isJoi) {
        return res.status(400).send({
          message: err.message,
          friendlyMsg: "Validator error",
        });
      }
      return res.status(500).send({
        message: err.message,
        friendlyMsg: "Internal server error",
      });
    }
  };
};
