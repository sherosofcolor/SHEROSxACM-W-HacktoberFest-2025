# =========================================================================
# ELI5 Algorithm Demo: Bubble Sort (The Smallest Bubbles Float Up)
# Author: Meghasaibhavya
# Topic: How computers solve problems step-by-step
# =========================================================================

def bubble_sort_eli5(data_list):
    """
    A simple demonstration of the Bubble Sort algorithm.

    Analogy: Compares adjacent elements and swaps them if they are in the
    wrong order. The largest element 'bubbles up' to its correct position
    after each full pass.
    """
    n = len(data_list)
    
    # Outer loop: Repeats the entire comparison process n times (for 'n' passes)
    for i in range(n):
        # Flag to optimize: if no swaps happen, the list is sorted
        swapped = False
        
        # Inner loop: Compares adjacent elements (0 to n-i-1)
        # We use n-i-1 because the last 'i' elements are already in place
        for j in range(0, n - i - 1):
            
            # Comparison step: If the current item is LARGER than the next item...
            if data_list[j] > data_list[j + 1]:
                
                # Swap step: ...then swap them!
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                swapped = True
                
                # Optional: Print the list after a swap to see the 'bubbling' effect
                print(f"Swap: {data_list}")
                
        # Optimization check: If no two elements were swapped in inner loop, break
        if not swapped:
            break

# -------------------------------------------------------------------------
# DEMONSTRATION
# -------------------------------------------------------------------------

# The unsorted list (our friends standing randomly in line)
friends_in_line = [5, 1, 4, 2, 8]
print(f"Original Unsorted List: {friends_in_line}")
print("-" * 30)

bubble_sort_eli5(friends_in_line)

print("-" * 30)
print(f"Final Sorted List: {friends_in_line}")

# Output confirms the sorting: [1, 2, 4, 5, 8]
