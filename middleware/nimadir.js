const winston = require("winston");
const expressWinston = require("express-winston");
const { transports } = require("winston");
const config = require("config");
require("winston-mongodb");

const expressW = expressWinston.logger({
  transports: [
    new transports.MongoDB({
      db: config.get("db_uri"),
      options: { useUnifiedTopology: true },
    }),
    new transports.Console(),
  ],
  format: winston.format.combine(
    winston.format.colorize(),
    winston.format.json(),
    winston.format.metadata(),
    winston.format.prettyPrint()
  ),
  meta: true,
  msg: "HTTP {{req.method}} {{req.url}}",
  expressFormat: true,
  colorize: false,
  ignoreRoute: function (req, res) {
    return false;
  },
});

const expressWinstonError = expressWinston.errorLogger({
  transports: [new transports.Console()],
  format: winston.format.combine(winston.format.prettyPrint() ),
});

module.exports = { expressW, expressWinstonError };
