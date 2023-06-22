const config = require("config");
require("winston-mongodb");
const winston = require("winston");
const { createLogger, format, transports } = require("winston");
const { combine, timestamp, label, printf, prettyPrint, json, colorize } =
  format;

const myFormat = printf(({ level, message, label, timestamp }) => {
  return `${timestamp} [${label}] ${level}: ${message}`;
});

let logger;

const devLog = winston.createLogger({
  format: combine(timestamp(), myFormat),
  transports: [
    new winston.transports.Console({ level: "debug" }),
    new transports.File({ filename: "log/error.log", level: "error" }),
    new transports.File({ filename: "log/combine.log", level: "info" }),
    new transports.MongoDB({
      db: config.get("db_uri"),
      options: { useUnifiedTopology: true },
    }),
  ],
});
const prodLog = createLogger({
  format: combine(timestamp(), myFormat),
  transports: [
    new transports.File({ filename: "log/error.log", level: "error" }),
    new transports.MongoDB({
      db: config.get("db_uri"),
      options: { useUnifiedTopology: true },
    }),
  ],
});

if (process.env.NODE_ENV == "production") {
  logger = prodLog;
} else {
  logger = devLog;
}

logger.exceptions.handle(
  new transports.File({ filename: "log/exceptions.log" })
);

logger.rejections.handle(
  new transports.File({ filename: "log/rejections.log" })
);

logger.exitOnError = false;
module.exports = logger;
