
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

    public static void main(String[] args){

        String filename = "records.log";
        int m = 3;
        int n = 6;
        double radius = 100;

        if(args.length == 2){
            m = Integer.parseInt(args[0]);
            n = Integer.parseInt(args[1]);
        }

        if(args.length == 3){
            m = Integer.parseInt(args[0]);
            n = Integer.parseInt(args[1]);
            radius = Double.parseDouble(args[2]);
        }

        if(args.length == 4){
            m = Integer.parseInt(args[0]);
            n = Integer.parseInt(args[1]);
            radius = Double.parseDouble(args[2]);
            filename = args[3];
        }

        Logger logger = new Logger(filename);

        // Initiate Arena
        Arena arena = new Arena(m, n, radius);

        // Run for this amount of time.
        Battle event = new Battle(arena, logger, true);
        event.run(120);

        double avg = 0;
        int reps = 100;
        for(int i = 0; i<reps; i++) {
            // Initiate Arena
            Arena aren = new Arena(m, n, radius);

            // Run for this amount of time.
            Battle even = new Battle(aren, logger, false);
            avg += even.run(120);
        }
        avg = avg/reps;
        System.out.println(avg);
    }
}
