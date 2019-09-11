import numpy as np
import matplotlib.pyplot as plt
import zernike
import cv2
import math

# c0 = 0.2072
# c1 = 2.0026
# c2 = -1.1228
# n_rbc = 1.395
# n_med = 1.334
# wavelength = 0.532
# R = 4
# grids = 50
#
# cmap = plt.cm.gray
#
# S = np.zeros((int(R * 2 * grids), int(R * 2 * grids)))
#
# for y in range(-int(R * grids), int(R * grids)):
#     for x in range(-int(R * grids), int(R * grids)):
#         px = (x - R / 2) / grids
#         py = (y - R / 2) / grids
#         r = np.sqrt(px * px + py * py)
#         if r < R:
#             S[y + int(R * grids), x + int(R * grids)] = R * np.sqrt(1 - np.power((r / R), 2)) * (
#                         c0 + c1 * np.power((r / R), 2) + c2 * np.power((r / R), 4))
#         else:
#             S[y + int(R * grids), x + int(R * grids)] = 0

# plt.figure()
# plt.imshow(S,cmap='gray')
# plt.show()
#
# phasemap = np.zeros_like(S)
# phasemap = S * 2 * np.pi / wavelength * (n_rbc - n_med)
#
# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6), sharex=True, sharey=True)
# ax1 = axes[0]
# ax2 = axes[1]
# im1 = ax1.imshow(S, cmap)
# im2 = ax2.imshow(phasemap, cmap)
#
# cbar_ax1 = fig.add_axes([0.15, 0.05, 0.3, 0.02])
# cbar1 = fig.colorbar(im1, cax=cbar_ax1, orientation='horizontal').set_label(label='thickness (μm)', size=14)
#
# cbar_ax2 = fig.add_axes([0.57, 0.05, 0.3, 0.02])
# cbar1 = fig.colorbar(im2, cax=cbar_ax2, orientation='horizontal').set_label(label='phi (rad)', size=14)
#
# plt.show()

path = "D:\\1LAB\\77_img.png"
aa = cv2.imread(path,0)
cc= cv2.resize(aa,(386,386))
Z1,C = zernike.fitting(cc,50)

C.zernikesurface()
C.zernikemap()


# row = int(500/ 2)
# col = int(500 / 2)
# mask1 = np.ones([500,500], np.uint8)
# mask1 = mask1 * 255
# for r in range(1, 10):  # range = max pixel
#     magni1 = (0 + (r / 50)) * 255
#     cv2.circle(mask1, (row, col), r, (magni1, magni1, magni1), r - 1)  # central remain one
# mask2 = np.zeros([500,500], np.uint8)
# for r in range(100, 0, -1):  # range = min pixel
#     magni2 = (2 / (1 + math.exp(r / 100))) * 255  # sigmoid decay
#     cv2.circle(mask2, (row, col), r, (magni2, magni2, magni2), r)
# mask = (mask2 / 255) * (mask1 / 255)
# plt.figure()
# plt.imshow(mask,cmap='gray')
# plt.show()
# # l = len(mask)
# # print(l)

