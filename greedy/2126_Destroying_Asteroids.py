class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for asteroid_mass in asteroids:
            if asteroid_mass > mass:
                return False
            mass += asteroid_mass
        
        return True

"""
- greedy algo problem
- we need to ensure we hit the mass (planet) with the smallest asteroid masses first
    - by doing this we gaurantee to be getting the mass of the planet as big as possible resulting in us being able to have the best attempt of destroying all the asteroid masses 
- time complexity: O(nlogn + n) --> O(nlogn), O(nlogn) due to sorting, O(n) due to iterating through the asteroid array but overall it gets ammortized to O(nlogn)
- space complexity: O(1) because we're modifying the array to sort in place
"""
