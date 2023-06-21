const { createLogger, format, transports } = require("winston");
const { combine, timestamp, printf, prettyPrint, json } = format;

const myFormat = printf(({ level, message, timestamp }) => {
  return `${timestamp} ] ${level}: ${message}`;
});

const logger = createLogger({
  format: combine(timestamp(), myFormat, prettyPrint(), json()),
  transports: [new transports.Console({ level: "debug" })],
});

module.exports = logger;
