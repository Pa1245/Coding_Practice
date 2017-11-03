import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
import java.util.*;


class Monk_birthday_HE {
    public static void main(String args[] ) throws Exception {

      Scanner in = new Scanner(System.in);
      int t = in.nextInt();
      while(t > 0) {
          int n = in.nextInt(), m = in.nextInt();
          long[] l = new long[m], w = new long[n], c = new long[n];
          for (int i = 0; i < m; i++)
              l[i] = in.nextLong();
          for (int i = 0; i < n; i++)
              w[i] = in.nextLong();
          long tot_wt = 0;
          for (int i = 0; i < n; i++) {
              c[i] = in.nextLong();
              tot_wt += c[i]*w[i];
          }
          System.out.println("Arrays: " + Arrays.toString(l) + "\t" +
          Arrays.toString(w) + "\t" + Arrays.toString(c));
          Arrays.sort(l);
          System.out.println("Sorted Arrays: " + Arrays.toString(l) + "\t" +
          Arrays.toString(w) + "\t" + Arrays.toString(c));
          for (int i = 1; i < n; i++) {
              long elementw = w[i], elementc = c[i];
              for (int j = 0; j < i; j++) {
                  if (elementw < w[j]) {
                      w[i] = w[j];
                      w[j] = elementw;
                      elementw = w[i];
                      c[i] = c[j];
                      c[j] = elementc;
                      elementc = c[i];
                  }
              }
          }
          System.out.println("xx");
          System.out.println("Sorted Arrays: " + Arrays.toString(l) + "\t" +
              Arrays.toString(w) + "\t" + Arrays.toString(c));
          long time = 0;
          System.out.println("tot_wt = " + tot_wt);
          if (l[m-1] < w[n-1]) {
            System.out.println("-1");
            continue;
          }
          while(tot_wt > 0) {
              for (int i = 0; i < m && tot_wt > 0; i++) {
                  if (l[i] >= w[i]) {
                      tot_wt -= w[i];
                      c[i]--;
                      System.out.println("l[" + i + "] = " + l[i] + "\tw[" + i + "] = " + w[i] + "\ttot_wt = " + tot_wt);
                  }
                  else if (i > 0){
                      int temp = i-1;
                      while (temp > 0) {
                          if (l[i] >= w[temp] && c[temp] > 0) {
                              tot_wt -= w[temp];
                              c[temp]--;
                              System.out.println("l[" + i + "] = " + l[i] + "\tw[" + temp + "] = " + w[temp] + "\ttot_wt = " + tot_wt);
                          }
                          temp--;
                      }
                  }
              }
              time++;
              System.out.println("time = " + time);
          }
          System.out.println("Time : " + time);
          t--;
      }
    }
}
