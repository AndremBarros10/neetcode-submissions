// Definition for a pair
// public class Pair {
//     public int Key;
//     public string Value;
//
//     public Pair(int key, string value) {
//         Key = key;
//         Value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> InsertionSort(List<Pair> pairs) {

    List<List<Pair>> states = new List<List<Pair>>();
        
        if (pairs.Count == 0)
            return states;

        // state after the first element (a single item is trivially "sorted")
        states.Add(new List<Pair>(pairs));

        for (int i = 1; i < pairs.Count; i++) {
            Pair current = pairs[i];
            int j = i - 1;

            while (j >= 0 && pairs[j].Key > current.Key) {
                pairs[j + 1] = pairs[j];
                j--;
            }

            pairs[j + 1] = current;

            states.Add(new List<Pair>(pairs));
        }

        return states;
    }

}
