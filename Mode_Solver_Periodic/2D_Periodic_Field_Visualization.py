from Periodic_Mode_Solver import TE_Mode_Solver

# Parameters for the simulation
x_range = 20e-3  # 20 mm in x-direction
z_range = 5e-3  # 5 mm in y-direction
Nx = 200  # Number of grid points in x-direction
Nz = 50  # Number of grid points in y-direction
frequency = 25e9  # Frequency
num_modes = 10  # Number of modes to solve for
guess = 0

solver = TE_Mode_Solver(freq=frequency, x_range=x_range, z_range=z_range, Nx=Nx, Nz=Nz, num_modes=num_modes,
                        guess=guess)

# Define structure
solver.add_object(-1e8, 1, x_indices=[164], z_indices=range(0, 6))
solver.add_object(10.2, 1, x_indices=range(165, 190), z_indices=range(solver.Nz))
solver.add_object(-1e8, 1, x_indices=[190], z_indices=range(solver.Nz))
solver.add_absorbing_boundaries(pml_width=50, sigma_max=20)

solver.solve_modes()
solver.visualize_with_gui()
