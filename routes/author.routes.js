const express = require("express");
const {
  getAllAuthor,
  addAuthor,
  getAuthorById,
  editAuthor,
  deleteAuthor,
  loginAuthor,
} = require("../controllers/author.controller");
const authorPolice = require("../middleware/authorPolice");
const authorRolesPolice = require("../middleware/authorRolesPolice");
const router = express.Router();

//hadlers
router.get("/", authorPolice, getAllAuthor);
router.post("/", addAuthor);
router.get(
  "/:id",
  authorRolesPolice(["READ", "WRITE", "CHANGE", "DELETE"]),
  getAuthorById
);
router.put("/:id", editAuthor);
router.delete("/:id", deleteAuthor);
router.post("/login", loginAuthor);

module.exports = router;
