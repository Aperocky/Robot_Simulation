import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

/***************************************************************************
 *
 * 	FILE: 			Battle.java
 *
 * 	AUTHOR:			ROCKY LI
 *
 * 	DATE:			10/11/2017
 *
 * 	VER: 			1.0
 *
 * 	Purpose: 		Manipulate the Arena from its initial state. Record the data.
 *
 **************************************************************************/

public class Battle {

    public Arena arena;

    public Logger logger;

    public boolean log_enabled;

    public Battle(Arena arena, Logger logger, boolean log){
        this.arena = arena;
        this.logger = logger;
        log_enabled = log;
    }

    public int ProcArena(int time){

        ArrayList<Robots> teaminfo = new ArrayList<Robots>(Arrays.asList(arena.robotlist));

        for(Targets each: arena.targetlist){
            each.flagged = false;
        }

        // Have the robots detect targets and share info about each other.

        for(Robots soldiers: arena.robotlist){
            ArrayList<Targets> detected = new ArrayList<Targets>();
            for(Targets enemy: arena.targetlist){
                if(soldiers.flag(enemy.Positions)){
                    detected.add(enemy);
                    enemy.flagged = true;
                }
            }
            soldiers.Detect(detected);
            soldiers.Communicate(teaminfo);
            soldiers.CalcV();
        }

        // Update the whole thing.

        int flagged = 0;

        for(Robots soldiers: arena.robotlist){
            soldiers.Update();
        }
        for(Targets enemy: arena.targetlist){
            enemy.Update();
            if(enemy.flagged){
                flagged ++;
            }
        }

        // Print flagged devices:
//        System.out.println(flagged);

        // Log positions.
        if(log_enabled) {
            try {
                logger.write(arena.robotlist, arena.targetlist, time);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        return flagged;
    }

    public double run(int time){
        int sum = 0;
        for(int i = 0; i<time; i++){
            sum += ProcArena(i);
        }
        double avg = sum/(double) time;
        return avg;
    }
}
