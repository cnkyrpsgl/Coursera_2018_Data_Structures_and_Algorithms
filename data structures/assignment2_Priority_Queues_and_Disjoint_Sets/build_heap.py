# python3
class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
  def ReadData(self):
    global n
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)
  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])
  def SiftDown(self, i):
      minIndex = i
      left = 2 * i + 1
      if left < n and self._data[left] < self._data[minIndex]:
          minIndex = left
      right = 2 * i + 2
      if right < n and self._data[right] < self._data[minIndex]:
          minIndex = right
      if i != minIndex:
          self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
          self._swaps.append([i, minIndex])
          self.SiftDown(minIndex)
  def GenerateSwaps(self):
    for i in range(n // 2, -1, -1):
        self.SiftDown(i)
  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()
if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()