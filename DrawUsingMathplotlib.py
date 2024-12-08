# import matplotlib.pyplot as plt

# # Fungsi untuk menggambar titik dan garis
# def plot_points_and_lines():
#     plt.axhline(0, color='black',linewidth=0.5)  # Sumbu x
#     plt.axvline(0, color='black',linewidth=0.5)  # Sumbu y
#     plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

#     # Menambahkan titik
#     plt.plot(5, 5, 'o', color='red', label="Titik (5,5)")
    
#     # Menggambar garis
#     x1, y1 = -10, -5
#     x2, y2 = 15, 7
#     plt.plot([x1, x2], [y1, y2], color="blue", label=f"Garis dari ({x1},{y1}) ke ({x2},{y2})")

#     # Pengaturan grafik
#     plt.xlim(-20, 20)
#     plt.ylim(-10, 10)
#     plt.legend()
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.title("Grafik dengan Titik dan Garis")
#     plt.show()

# # Panggil fungsi untuk menggambar grafik
# plot_points_and_lines()








# import matplotlib.pyplot as plt

# # Function for algorithm Bresenham
# def bresenham_line(x1, y1, x2, y2):
#     points = []  
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     sx = 1 if x1 < x2 else -1
#     sy = 1 if y1 < y2 else -1
#     err = dx - dy

#     while True:
#         points.append((x1, y1)) 
#         if x1 == x2 and y1 == y2:  # If reach end break the loop
#             break
#         e2 = 2 * err
#         if e2 > -dy:
#             err -= dy
#             x1 += sx
#         if e2 < dx:
#             err += dx
#             y1 += sy
#     return points

# # Function to draw line in matplotlib
# def plot_bresenham_line(x1, y1, x2, y2):
#     points = bresenham_line(x1, y1, x2, y2) 
#     x_values, y_values = zip(*points)  # spare x n y

#     # Plot titik-titik menggunakan matplotlib
#     plt.figure(figsize=(6, 6))
#     plt.plot(x_values, y_values, '.', color='blue', markersize=5, label="Garis Bresenham")
    
#     # Tambahkan sumbu x dan y
#     plt.axhline(0, color='black',linewidth=0.5)
#     plt.axvline(0, color='black',linewidth=0.5)
    
#     # Pengaturan grafik
#     plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
#     plt.xlim(min(x_values) - 1, max(x_values) + 1)
#     plt.ylim(min(y_values) - 1, max(y_values) + 1)
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.title(f"Garis dari ({x1}, {y1}) ke ({x2}, {y2}) dengan Algoritma Bresenham")
#     plt.legend()
#     plt.show()

# # Contoh menggambar garis dari titik (2, 2) ke (15, 10)
# plot_bresenham_line(2, 2, 15, 10)




# Code from geekforgeek
# Python program for DDA line generation 

from matplotlib import pyplot as plt 

# DDA Function for line generation 


def DDA(x0, y0, x1, y1): 

	# find absolute differences 
	dx = abs(x0 - x1) 
	dy = abs(y0 - y1) 

	# find maximum difference 
	steps = max(dx, dy) 

	# calculate the increment in x and y 
	xinc = dx/steps 
	yinc = dy/steps 

	# start with 1st point 
	x = float(x0) 
	y = float(y0) 

	# make a list for coordinates 
	x_coorinates = [] 
	y_coorinates = [] 

	for i in range(steps): 
		# append the x,y coordinates in respective list 
		x_coorinates.append(x) 
		y_coorinates.append(y) 

		# increment the values 
		x = x + xinc 
		y = y + yinc 

	# plot the line with coordinates list 
	plt.plot(x_coorinates, y_coorinates, marker="o", 
			markersize=1, markerfacecolor="red") 
	plt.show() 


# Driver code 
if __name__ == "__main__": 

	# coordinates of 1st point 
	x0, y0 = 20, 20

	# coordinates of 2nd point 
	x1, y1 = 60, 50

	# Function call 
	DDA(x0, y0, x1, y1) 

	# This code is contributed by 111arpit1 
