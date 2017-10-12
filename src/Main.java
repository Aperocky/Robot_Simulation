
/***************************************************************************
 *
 * 	FILE: 			Main.java
 *
 * 	AUTHOR:			ROCKY LI
 *
 * 	DATE:			10/11/2017
 *
 * 	VER: 			1.0
 *
 * 	Purpose: 		Entry point, run simulation
 *
 **************************************************************************/

public class Main {

    public static void main(String args[]){

        int m = 3;
        int n = 6;

        // Initiate Arena
        Arena arena = new Arena(m, n, 100);

        // Run for this amount of time.
        Battle event = new Battle(arena);
        event.run(120);
    }
}
