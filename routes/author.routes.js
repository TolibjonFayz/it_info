const express = require("express");
const {
  getAllAuthor,
  addAuthor,
  getAuthorById,
  editAuthor,
  deleteAuthor,
  loginAuthor,
  logoutAuthor,
  refreshAuthorToken,
  authorActivate,
} = require("../controllers/author.controller");

const Validator = require("../middleware/validator");

const authorPolice = require("../middleware/authorPolice");
const authorRolesPolice = require("../middleware/authorRolesPolice");
const router = express.Router();

//hadlers
router.get("/", authorPolice, getAllAuthor);
router.post("/", Validator("author"), addAuthor);
router.get(
  "/:id",
  authorRolesPolice(["READ", "WRITE", "CHANGE", "DELETE"]),
  getAuthorById
);
router.put("/:id", editAuthor);
router.delete("/:id", deleteAuthor);
router.post("/login", Validator("author_email_pass"), loginAuthor);
router.post("/logout", logoutAuthor);
router.post("/refresh", refreshAuthorToken);
router.get("/activate/:id", authorActivate);

module.exports = router;
