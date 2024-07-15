import sys
import cv2
import os

try:
    # Check if a filename was provided
    if len(sys.argv) < 2:
        raise ValueError("No filename provided. Please specify an image file.")

    # Get the filename from the command-line arguments
    filename = sys.argv[1]
    filepath = 'public/uploads/' + filename
    print(f"Loading image from: {filepath}")

    # Load the image
    image = cv2.imread(filepath)
    if image is None:
        raise ValueError(f"Image not found at path: {filepath}")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image
    _, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        raise ValueError("No contours found in the image.")

    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the bounding rectangle for the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the image to this bounding rectangle
    cropped = image[y:y+h, x:x+w]

    # Overwrite the original image file with the cropped image
    _, file_extension = os.path.splitext(filepath)
    cropped_filename = filepath if file_extension else filepath + ".jpg"
    cv2.imwrite(cropped_filename, cropped)

    # Print the path to the processed image
    print(cropped_filename)

except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)
