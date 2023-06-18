const express = require("express");
const config = require("config");
const mongoose = require("mongoose");
const errorHandler = require("./middleware/error_handling_middleware");
const cookieParser = require("cookie-parser");

const PORT = config.get("port") || 3030;

//Barcha routlarni chaqirdik
const routes = require("./routes/index.routes");

const app = express();
app.use(express.json());
app.use(cookieParser());

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
