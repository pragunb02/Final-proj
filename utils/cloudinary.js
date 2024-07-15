const cloudinary = require("cloudinary").v2;
const fs = require("fs");
const dotenv = require("dotenv");

dotenv.config();

cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
});

const uploadOnCloudinary = async (localFilePath) => {
  console.log("Starting upload to Cloudinar/..................");
  try {
    if (!localFilePath) return null;

    // Upload file to Cloudinary
    const result = await cloudinary.uploader.upload(localFilePath, {
      resource_type: "auto",
    });
    console.log("Upload successful:", result);
    console.log("URL:", result.secure_url);
    if (fs.existsSync(localFilePath)) {
      console.log("waiting???????");
      fs.unlinkSync(localFilePath);
    }
    return result;
  } catch (error) {
    // Remove the locally saved file if the upload fails
    if (fs.existsSync(localFilePath)) {
      console.log("waiting");
      fs.unlinkSync(localFilePath);
    }
    console.error("Error uploading to Cloudinary:", error);
    return null;
  }
};

// Export the function
module.exports = {
  uploadOnCloudinary,
};
