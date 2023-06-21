const express = require("express");
const config = require("config");
const mongoose = require("mongoose");
const errorHandler = require("./middleware/error_handling_middleware");
const cookieParser = require("cookie-parser");
require("dotenv").config({ path: `.env.${process.env.NODE_ENV}` });
const logger = require("./services/logger");

logger.log("d","LOG malumotlar");
logger.error("ERROR malumotlar");
logger.warn("WARN malumotlar");
logger.debug("DEBUG malumotlar");
logger.info("INFO malumotlar");
// logger.trace("TRACE malumotlar");
// logger.table([
//   ["Salim", "20"],
//   ["Nodir", "16"],
//   ["Baxtiyor", "55"],
// ]);

// console.log(process.env.NODE_ENV);
// console.log(process.env.secret);
// console.log(config.get("secret"));
// console.log(config.get("access_key"));

const PORT = config.get("port") || 3030;

//Barcha routlarni chaqirdik
const routes = require("./routes/index.routes");

process.on("uncaughtException", (ex) => {
  console.log("uncaughtException:", ex.message);
});

process.on("unhandledRejection", (rej) => {
  console.log("unhandledRejection:", rej);
});

const app = express();
app.use(express.json()); //Frontenddan kelayotgan requestlarni jsonga parse qiladi(taniydi)
app.use(cookieParser()); //Frontenddan kelayotgan requestlar ichidagi cookie(pichina)ni o'qiydi

app.use(errorHandler);
app.use(routes);

//Daatbazaga ulanib serverni ishga tushirish
async function start() {
  try {
    await mongoose.connect(config.get("atlasURI"));

    app.listen(PORT, () => {
      console.log(`Server ${PORT}-portda ishga tushdi!`);
    });
  } catch (error) {
    console.log("Serverda xatolik");
  }
}

start();
