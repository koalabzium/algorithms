import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

class Main {
  public static void main(String[] args) {
    ArrayList<String> lista1 = new ArrayList<String>(Arrays.asList("a","b","c","d","b"));
    ArrayList<String> lista2 = new ArrayList<String>(Arrays.asList("g","b","c","e"));

    Lista.unique(lista1, lista2);

  }
}

class Lista{
  public static void unique(ArrayList<String> arr1, ArrayList<String> arr2){
      HashSet<String> elements = new HashSet<String>();
      for (String el : arr1){
        elements.add(el);
      }
      for (String el: arr2){
        if (elements.contains(el)){
          elements.remove(el);
        }
        else{
          elements.add(el);
        }
      }
      System.out.print(elements);
  }
}
