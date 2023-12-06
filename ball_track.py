import cv2
import numpy as np
import time

t1_g = []
t1_o = []
t1_w = []
t1_y = []

q_g = []
q_o = []
q_w = []
q_y = []

data = []

start = time.time()
path = "C:\\Users\\manav\\OneDrive\\Desktop\\AI Assi\\output.txt.txt"

# Open the file for writing
with open(path, "w") as output:
    output.write("Time, Quadrant Number, Ball Colour, Event Type\n")

    def find_quadrant(x, y):
        
        if 1250 < x < 1750 and 550 < y < 1000:
            return 1
        
        elif 800 < x < 1215 and 550 < y < 1000:
            return 2
        
        elif 800 < x < 1215 and 30 < y < 500:
            return 3
        
        elif 1250 < x < 1750 and 30 < y < 500:
            return 4
        
        else:
            return None

    video = cv2.VideoCapture('C:\\Users\\manav\\OneDrive\\Desktop\\AI Assi\\AI Assignment video.mp4')

    while video.isOpened():
        mas, frame = video.read()
        cv2.namedWindow("video o/p", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("video o/p", 1280, 720)

        if mas:
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (17, 17), 0)

            # Apply threshold to isolate squares
            _, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)

            # Find contours of squares
            contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Draw rectangles around squares
            for contour in contours:
                # Find the area of the contour
                area = cv2.contourArea(contour)

                # Find the perimeter of the contour
                perimeter = cv2.arcLength(contour, True)

                # Approximate the contour as a polygon with fewer vertices
                approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

                # If the contour is a square, draw a rectangle around it
                if len(approx) == 4 and abs(area) > 2000:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Detect circles
            circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 90, param1=100, param2=40, minRadius=10, maxRadius=100)

            if circles is not None:
                circles = np.uint16(np.around(circles))

                for (x, y, rad) in circles[0, :]:
                    cv2.circle(frame, (x, y), rad, (100, 255, 0), 3)
                    b, g, r = frame[y, x]

                    # Yellow
                    if 50 < r < 230 and 50 < g < 200 and 10 < b < 75:
                        q_y.append(find_quadrant(x, y))
                        end_yellow = time.time()
                        time_yellow_in = end_yellow - start
                        t1_y.append(int(time_yellow_in))
                        cv2.putText(frame, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

                        try:
                            yellow_in = [f"{t1_y[0]}", f"{q_y[-1]}", "Yellow", "Enter"]
                            yellow_out = [f"{t1_y[-1]}", f"{q_y[-1]}", "Yellow", "Exit"]
                            if t1_y[-1] - t1_y[-2] > 3:
                                output.write(", ".join(map(str, yellow_in)) + "\n")
                                output.write(", ".join(map(str, yellow_out)) + "\n")
                                t1_y.clear()
                        except IndexError:
                            pass

                    # Green
                    if 10 < r < 75 and 25 < g < 75 and 25 < b < 75:
                        q_g.append(find_quadrant(x, y))
                        end_green = time.time()
                        time_green_in = end_green - start
                        t1_g.append(int(time_green_in))
                        cv2.putText(frame, "Green", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

                        try:
                            green_in = [f"{t1_g[0]}", f"{q_g[-1]}", "Green", "Enter"]
                            green_out = [f"{t1_g[-1]}", f"{q_g[-1]}", "Green", "Exit"]
                            if t1_g[-1] - t1_g[-2] > 2:
                                output.write(", ".join(map(str, green_in)) + "\n")
                                output.write(", ".join(map(str, green_out)) + "\n")
                                t1_g.clear()
                        except IndexError:
                            pass

                    # Orange
                    if 175 < r < 255 and 50 < g < 175 and 25 < b < 150:
                        q_o.append(find_quadrant(x, y))
                        end_orange = time.time()
                        time_orange_in = end_orange - start
                        t1_o.append(int(time_orange_in))
                        cv2.putText(frame, "Orange", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

                        try:
                            orange_in = [f"{t1_o[0]}", f"{q_o[-1]}", "Orange", "Enter"]
                            orange_out = [f"{t1_o[-1]}", f"{q_o[-1]}", "Orange", "Exit"]
                            if t1_o[-1] - t1_o[-2] > 2:
                                output.write(", ".join(map(str, orange_in)) + "\n")
                                output.write(", ".join(map(str, orange_out)) + "\n")
                                t1_o.clear()
                        except IndexError:
                            pass

                    # White
                    if 100 < r < 255 and 100 < g < 255 and 100 < b < 255:
                        q_w.append(find_quadrant(x, y))
                        end_white = time.time()
                        time_white_in = end_white - start
                        t1_w.append(int(time_white_in))
                        cv2.putText(frame, "White", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

                        try:
                            white_in = [f"{t1_w[0]}", f"{q_w[-1]}", "White", "Enter"]
                            white_out = [f"{t1_w[-1]}", f"{q_w[-1]}", "White", "Exit"]
                            if t1_w[-1] - t1_w[-2] > 2:
                                output.write(", ".join(map(str, white_in)) + "\n")
                                output.write(", ".join(map(str, white_out)) + "\n")
                                t1_w.clear()
                        except IndexError:
                            pass

            # Display the video
            cv2.imshow('video o/p', frame)

            # Exit if 'r' is pressed
            if cv2.waitKey(1) == ord('r'):
                break
        else:
            break

    video.release()
    cv2.destroyAllWindows()
