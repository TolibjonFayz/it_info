const express = require("express");
const config = require("config");
const mongoose = require("mongoose");
const routes = require("./routes/index.routes");
const cookieParser = require("cookie-parser");
const PORT = config.get("port") || 3030;

const exHbs = require("express-handlebars");

const errorHandler = require("./middleware/error_handling_middleware");

const { engine } = require("express-handlebars");

// const logger = require("./services/logger");
// const expressWinston = require("express-winston");
// const winston = require("winston");

// //Barcha routlarni chaqirdik
// const { expressW, expressWinstonError } = require("./middleware/nimadir");

require("dotenv").config({ path: `.env.${process.env.NODE_ENV}` });

const app = express();
app.use(express.json()); //Frontenddan kelayotgan requestlarni jsonga parse qiladi(taniydi)
app.use(cookieParser()); //Frontenddan kelayotgan requestlar ichidagi cookie(pichina)ni o'qiydi

//what the hecks
// app.use(
//   expressWinston.logger({
//     transports: [
//       new winston.transports.Console({
//         json: true,
//         colorize: true,
//       }),
//     ],
//     meta: true, // optional: control whether you want to log the meta data about the request (default to true)
//     msg: "HTTP {{req.method}} {{req.url}}", // optional: customize the default logging message. E.g. "{{res.statusCode}} {{req.method}} {{res.responseTime}}ms {{req.url}}"
//     expressFormat: true, // Use the default Express/morgan request formatting. Enabling this will override any msg if true. Will only output colors with colorize set to true
//     colorize: false, // Color the text and status code, using the Express/morgan color palette (text: gray, status: default green, 3XX cyan, 4XX yellow, 5XX red).
//     ignoreRoute: function (req, res) {
//       return false;
//     }, // optional: allows to skip some log messages based on request and/or response
//   })
// );

// app.use(expressw);
// app.use(expressWinstonError);

const hbs = exHbs.create({
  defaultLayout: "main",
  extname: "hbs", //handlebars
});

app.engine("hbs", hbs.engine);
app.set("View engine", "hbs");
app.set("views", "views");
app.use(express.static("views"));

app.use(routes);

app.use(errorHandler);

//Daatbazaga ulanib serverni ishga tushirish
async function start() {
  try {
    await mongoose.connect(config.get("atlasURI"));
    app.listen(PORT, () => {
      console.log(`Server ${PORT}-portda ishga tushdi!`);
    });
  } catch (error) {
    console.log(error);
    console.log("Serverda xatolik");
  }
}

start();
