const author_email_pass = require("../validations/author_email_path.validator");
const author = require("./author.validator");
const category = require("./category.validator");
const admin_email_pass = require("../validations/admin_email_pass");
const admin = require("./admin");

module.exports = {
  author_email_pass,
  author,
  category,
  admin_email_pass,
  admin,
};
