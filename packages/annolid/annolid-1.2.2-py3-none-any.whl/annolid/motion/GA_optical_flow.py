
import numpy as np
import cv2


def find_motion_patterns(optical_flow):
    # Convert optical flow to vectors
    U, V = optical_flow[..., 0], optical_flow[..., 1]

    # Calculate vector magnitudes and angles
    magnitude = np.sqrt(U**2 + V**2)
    angle = np.arctan2(V, U)

    # Identify motion patterns
    translation_threshold = 0.1  # Threshold for translation detection
    rotation_threshold = 0.5  # Threshold for rotation detection

    # Initialize motion pattern labels
    motion_patterns = np.zeros_like(magnitude, dtype=int)

    # Detect translation
    motion_patterns[magnitude < translation_threshold] = 1

    # Detect rotation
    motion_patterns[(magnitude >= translation_threshold) &
                    (magnitude < rotation_threshold)] = 2

    # Detect other patterns (e.g., expansion/contraction, shearing)
    # Add more conditions as needed

    return motion_patterns


class OpticalFlowCalculator:
    def __init__(self, alpha=2, sigma=3, sigma_t=2):
        self.alpha = alpha
        self.sigma = sigma
        self.sigma_t = sigma_t

    def compute_optical_flow(self, I_prev, I_next):
        # Compute gradients
        Ix, Iy = self.sobel_operator(I_next)
        It = I_next - I_prev

        # Compute unsmoothed solutions
        u10, u20 = self.compute_unsmoothed_solution(Ix, Iy, It)

        # Smooth the flow
        U = self.smooth_flow(u10, 1)
        V = self.smooth_flow(u20, 1)

        return U, V

    def sobel_operator(self, input):
        # Define the Sobel kernel for the x direction
        sobel_kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

        # Define the Sobel kernel for the y direction
        sobel_kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

        # Apply the Sobel operator in the x and y directions
        grad_x = cv2.filter2D(input, -1, sobel_kernel_x)
        grad_y = cv2.filter2D(input, -1, sobel_kernel_y)

        # Return the gradients
        return grad_x, grad_y

    def piecewise_robustness_operator(self, x):
        return np.where(x < -self.alpha, -self.alpha, np.where(x > self.alpha, self.alpha, x))

    def compute_unsmoothed_solution(self, Ix, Iy, It):
        # added a small epsilon to avoid division by zero
        norm_grad_I_squared = Ix**2 + Iy**2 + 1e-6
        u10 = self.piecewise_robustness_operator(
            (-Ix*It - Iy*(Iy + Ix*(Ix - Iy))) / norm_grad_I_squared)
        u20 = self.piecewise_robustness_operator(
            (Ix*(Iy + Ix*(Ix - Iy)) - Iy*It) / norm_grad_I_squared)
        return u10, u20

    def smooth_flow(self, flow, j):
        # Apply spatial smoothing
        flow_smoothed = cv2.GaussianBlur(flow, (0, 0), self.sigma)

        # Apply temporal smoothing
        flow_smoothed = cv2.GaussianBlur(flow_smoothed, (0, 0), self.sigma_t)

        return flow_smoothed


def main():
    # Create an instance of the OpticalFlowCalculator
    optical_flow_calculator = OpticalFlowCalculator()

    # Open the video file using OpenCV
    cap = cv2.VideoCapture('/Users/chenyang/Downloads/annolid_demo/mouse.mp4')

    # Read the first frame
    ret, frame_prev = cap.read()
    # Create HSV color wheel image
    hsv = np.zeros_like(frame_prev)
    hsv[..., 1] = 255

    # Initialize variables for tracking movement direction
    total_dx = 0
    total_dy = 0

    while True:
        # Read the next frame
        ret, frame_next = cap.read()

        if not ret:
            break
        # Convert frames to grayscale
        gray_prev = cv2.cvtColor(frame_prev, cv2.COLOR_BGR2GRAY)
        gray_next = cv2.cvtColor(frame_next, cv2.COLOR_BGR2GRAY)

        if True:
            # Compute optical flow using Farneback method
            flow = cv2.calcOpticalFlowFarneback(
                gray_prev, gray_next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

            # Convert optical flow magnitude and direction to HSV
            mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        else:

            # Compute optical flow
            U, V = optical_flow_calculator.compute_optical_flow(
                gray_prev, gray_next)

            # Convert flow tensors to numpy arrays
            flow_x = U
            flow_y = V

            # Visualize the flow using OpenCV's quiver function
            flow_image = cv2.cvtColor(gray_next, cv2.COLOR_GRAY2BGR)
            # print(flow_x, flow_y, flow_x.shape, flow_y.shape)
            # for i in range(0, flow_x.shape[0], 20):
            #     for j in range(0, flow_x.shape[1], 20):
            #         cv2.arrowedLine(
            #             flow_image, (j, i), (j + int(flow_x[i, j]) * 100, i + int(flow_y[i, j]) * 100), (0, 255, 0), 1)
            mag, ang = cv2.cartToPolar(flow_x, flow_y)

        # Calculate average flow vector
        avg_flow = np.mean(flow, axis=(0, 1))

        # Accumulate movement in x and y directions
        total_dx += avg_flow[0]
        total_dy += avg_flow[1]

        # Display frame with optical flow
        # (For visualization purposes only)
        draw_frame = frame_next.copy()
        for y in range(0, frame_next.shape[0], 10):
            for x in range(0, frame_next.shape[1], 10):
                dx, dy = flow[y, x]
                cv2.arrowedLine(draw_frame, (x, y), (int(
                    x + dx), int(y + dy)), (0, 255, 0), 1)
        # hsv[..., 0] = ang * 180 / np.pi / 2
        # hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

        # # Convert HSV to BGR
        # bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        # Display the flow image
        cv2.imshow('Optical Flow', draw_frame)

        # Read the next frame
        frame_prev = frame_next

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # # Find motion patterns
        # motion_patterns = find_motion_patterns(flow)

        # # Visualize motion patterns (replace this with your preferred visualization)
        # # For example, you can use matplotlib to plot motion patterns
        # import matplotlib.pyplot as plt

        # plt.imshow(motion_patterns, cmap='viridis', interpolation='nearest')
        # plt.colorbar()
        # plt.title('Motion Patterns')
        # plt.show()

    # Release the video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
