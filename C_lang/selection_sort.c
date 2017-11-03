#include <stdio.h>

int main(void) {
  void selectSort(int arr[], int n);
  printf("Enter the length of array\n");
  int n;
  scanf("%d", &n);
  int arr[n];
  printf("Enter the array elementsn");
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }
  selectSort(arr, n);
  printf("Sorted Array:\n");
  for (int i = 0; i < n; i++)
    printf("%d\n", arr[i]);
}

void selectSort(int arr[], int n) {
  for (int i = 1; i <= n; i++) {
    int element = arr[i];
    for (int j = 0; j < i; j++) {
      if (element < arr[j]) {
        arr[i] = arr[j];
        arr[j] = element;
        element = arr[i];
      }
    }
  }
}
