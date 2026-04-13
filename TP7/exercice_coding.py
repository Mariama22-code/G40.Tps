def fusionner(nums1, nums2):
    resultat = []
    i = 0
    j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            resultat.append(nums1[i])
            i += 1
        else:
            resultat.append(nums2[j])
            j += 1
    
    resultat += nums1[i:]
    resultat += nums2[j:]
    
    return resultat

# Tests
print(fusionner([1, 2, 3], [2, 5, 6])) 
print(fusionner([1], []))              