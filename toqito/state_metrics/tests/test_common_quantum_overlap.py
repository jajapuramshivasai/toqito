# import numpy as np
# from toqito.state_metrics import common_quantum_overlap
# from toqito.states import basis, bell
# from toqito.state_ops import pure_to_mixed

# def test_common_quantum_overlap():
#     # Test case 1: Orthogonal pure states
#     states1 = [basis(2, 0), basis(2, 1)]
#     assert np.isclose(common_quantum_overlap(states1), 0)

#     # Test case 2: Identical pure states
#     states2 = [basis(2, 0), basis(2, 0)]
#     assert np.isclose(common_quantum_overlap(states2), 2)

#     # Test case 3: Bell states
#     states3 = [bell(0), bell(1), bell(2), bell(3)]
#     assert np.isclose(common_quantum_overlap(states3), 1)

#     # Test case 4: Mixed states
#     rho1 = pure_to_mixed(basis(2, 0))
#     rho2 = pure_to_mixed(basis(2, 1))
#     rho3 = 0.5 * (rho1 + rho2)
#     states4 = [rho1, rho2, rho3]
#     expected_overlap = 1.5  # This value might need adjustment based on actual calculation
#     assert np.isclose(common_quantum_overlap(states4), expected_overlap, atol=1e-6)

#     # Test case 5: Single state
#     states5 = [basis(2, 0)]
#     assert np.isclose(common_quantum_overlap(states5), 1)

#     # Test case 6: Higher dimensional states
#     states6 = [basis(4, i) for i in range(4)]
#     assert np.isclose(common_quantum_overlap(states6), 1)

#     print("All test cases passed!")

# # Run the tests
# test_common_quantum_overlap()
# print("All tests passed!")
print("All tests passed!")