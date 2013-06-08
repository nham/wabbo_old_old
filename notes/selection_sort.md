selection sort(A):
  n := A.length
  for i=1 to n-1:
    min := i

    for j=i+1 to n:
      if A[j] < A[min]:
        min := j

    swap A[i] and A[min]


Loop invariant: at i, A[1..(i-1)] is sorted and contains the smallest (i-1) elements in A (all v \in A[i..n] are bigger than every u in A[1..(i-1)])

hence when loop terminates at i = n, A[i..(n-1)] is sorted and each is less than A[n]. hence A is sorted.

      
