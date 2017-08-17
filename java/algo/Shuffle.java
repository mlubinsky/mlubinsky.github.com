import java.util.*;

public class Shuffle {


    // Get number of cards as command line argument
    // Step 1: remove 1st card from top of deck and put it on table
    // Step 2:  remove 1st card from top of deck and put it on bottom in deck
    // Step 3: Got to step 1 and 2 till all cards on table. This is the end of ROUND
    // Step 4. Pick up all cards from table  and repeat the round until the deck in original order

    static void pt(String str, LinkedList<Integer> a) {
          System.out.println(str);
          System.out.println(a);

    }
    static void from_deck_to_table(LinkedList<Integer> deck, LinkedList<Integer> table) {
     // int el = deck.removeLast();
     // table.add(el);    //or add addFirst or addLast or offer?
      int el = deck.removeFirst();
      table.addFirst(el);    //or add addFirst or addLast or offer?

    }

    static void from_deck_top_to_bottom(LinkedList<Integer> deck){
      //System.out.println("from_deck_top_to_bottom");
      //int el = deck.removeLast();
      //deck.addFirst(el);

      int el = deck.removeFirst();
      deck.addLast(el);

    }

    static  LinkedList<Integer> Round2 (int deck_cards, LinkedList<Integer> deck, LinkedList<Integer> table){
      LinkedList<Integer> t = new  LinkedList<>();
      while (deck_cards > 0) {
         t=table;
         table=deck;
         from_deck_to_table(deck, table);
         deck_cards--;
         if (deck_cards>0) {
                             t=deck;
                             pt("Transit",t);
                             from_deck_top_to_bottom(deck);
         }  else {
             t=table;
         }
      } // end while


      t=table;
      return t;

    }

    static  LinkedList<Integer> Round (int deck_cards, LinkedList<Integer> deck, LinkedList<Integer> table){
      LinkedList<Integer> t = new  LinkedList<>();
      while (deck_cards > 0) {
        System.out.println ("=======n_cards========="+ deck_cards);

/*
         t.clear();
         if (!table.isEmpty())
               t.add(table.getFirst());
*/
         from_deck_to_table(deck, table);
 /*
         pt("0 - DESK", deck);
         pt("0 - Table", table);
         pt("0 - Transit", t);
 */
         deck_cards--;

         //if (deck_cards == 1)  System.exit(1);
         if (deck_cards>0) {

               /*
                             t.clear();
                             t.add(deck.getFirst());
                             pt("2 Transit", t);
                */
                             from_deck_top_to_bottom(deck);

         }  /* else {

         t=table;
         pt("1 - DESK", deck);
         pt("1 - Table", table);
         pt("1 - Transit", t);

         }
         */
      } // end while


      t=table;
      return t;

    }


// Calculate GCD based on euclidean algorithma and recursion
 static int gcd(int num1, int num2) {
  if (num2 == 0 || num1 == num2) {
    return num1;
  }

  if (num1 > num2) {
    return gcd(num2,num1%num2);
  } else {
    return gcd(num1,num2%num1);
  }
}

  public static void main(String[] args) {

   int n_cards=0;
   if (args.length == 1) {

      try {
         n_cards = Integer.parseInt(args[0]);
         if (n_cards < 1){
           System.err.println ("Single positive integer argument is requred: the number of cards");
           System.exit(1);
         }
      } catch (NumberFormatException e) {
         System.err.println ("Argument must be integer");
         System.exit(1);
      }
   } else {
         System.err.println ("Single positive integer argument is requred: the number of cards");
         System.exit(1);
   }


    LinkedList<Integer> table = new LinkedList<>();   //Stack?
    LinkedList<Integer> deck = new LinkedList<>();    //Stack?

    for (Integer i=0; i<n_cards; i++){
      //deck.add(n_cards-i-1);
      deck.add(i);
    }

     LinkedList<Integer> t =  Round(n_cards, deck, table);
     pt("AFTER ROUND transit=", t);
     //System.exit(1);


    //Collections.fill(isAlreadyCalculated, Boolean.FALSE);
/*
void map_positions() {
  uint32_t i;
        index_mapper = (struct index_map *)malloc(card_count * sizeof(struct index_map));
        memset(index_mapper,0,sizeof(index_mapper));
        int count = 0;
        p(" map_positions()-- Transit",transit);
        while (transit != NULL) {
                //if (DEBUG)
                //        printf("%d \n",transit->index);

                //Updating Mapping obtained from first round
                index_mapper[transit->index].next = count;
                transit = transit->next;
                count++;
        }
        if (DEBUG) {
                for (i=0;i<count;i++) {
                        printf("MAPPER %d ---> %d \n",i,index_mapper[i].next);
                }

        }
}
*/
    //ArrayList<Integer> mapper = new ArrayList<>(n_cards);
    //ArrayList<Boolean> isAlreadyCalculated = new ArrayList<>(n_cards);

    int[] mapper = new int[n_cards];
    int[] isAlreadyCalculated = new int[n_cards];
    Arrays.fill(mapper, -1);
    Arrays.fill(isAlreadyCalculated, 0);

    int count=0;
    //for (int i=0; i<n_cards; i++){
    for (Integer index : t){

       //System.err.println ("index="+ index);
       //mapper.add(index,count);
       mapper[index]=count;
       //int j=table.get(i);
       //mapping.add(j,count);
       System.out.println (index + " " + "  -> "+ count);
       count++;

       //isAlreadyCalculated.add(index,Boolean.FALSE);
    }
    //System.exit(1);
/*
    for (int i=0; i<n_cards; i++){
      System.out.println(isAlreadyCalculated.get(i));
    }
    System.exit(1);
*/


    int lcm=1;

    int round;
    for (int i=0; i < n_cards; i++){
      if (isAlreadyCalculated[i] == 1)  {
         continue;
      }
      int next = mapper[i];
      isAlreadyCalculated[i]=1;

      round=1;
      while (i != next){
          isAlreadyCalculated[next]=1;
          next = mapper[next];
          round++;
      }
      //System.out.println("Round for "+ i +" "+round);
      lcm = (lcm*round)/gcd(lcm,round);
    }




    System.out.println("Number of rounds: "+ lcm);
  }  //end of main
}