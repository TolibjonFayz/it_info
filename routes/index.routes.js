const express = require("express");
const { Router } = require("express");

express.Router.prefix = function (path, subRouter) {
  const router = express.Router();
  this.use(path, router);
  subRouter(router);
  return router;
};

const router = express.Router();
const dictionary = require("./dictionary.routes");
const category = require("./category.routes");
const description = require("./description.routes");
const synonyms = require("./synonym.routes");
const authors = require("./author.routes");
const admin = require("./admin.routes");
const user = require("./user.routes");

const router1 = Router();
router1.prefix("/api", (apitRouter) => {
  apitRouter.use("/dict", dictionary);
});

router.use("/dictionary", dictionary);
router.use("/category", category);
router.use("/description", description);
router.use("/synonyms", synonyms);
router.use("/author", authors);
router.use("/admin", admin);
router.use("/user", user);

module.exports = router;
