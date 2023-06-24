const { Router } = require("express");

const { createViewPath } = require("../helpers/create_view_path");

const router = Router();

router.get("/", (req, res) => {
  res.render(createViewPath("index"), {
    title: "Asosiy sahifa",
    isHome: true, //classda menu active qilish uchun
  });
});

router.get("/dictionaries", (req, res) => {
  res.render(createViewPath("dictionary"), {
    title: "Lug'atlar",
    isDict: true,
  });
});

router.get("/topics", async (req, res) => {
  res.render(createViewPath("topics"), {
    title: "Maqolalar",
    isTopic: true,
  });
});

router.get("/authors", async (req, res) => {
  res.render(createViewPath("authors"), {
    title: "Mualliflar",
    isAuthor: true,
  });
});

module.exports = router;
