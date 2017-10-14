import java.io.*;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;

/***************************************************************************
 *
 * 	FILE: 			Logger.java
 *
 * 	AUTHOR:			ROCKY LI
 *
 * 	DATE:			10/11/2017
 *
 * 	VER: 			1.0
 *
 * 	Purpose: 		Log the positions of targets and robots.
 *
 **************************************************************************/

public class Logger {

    File log;

    public Logger(String filename){
        this.log = new File(filename);
        if (log.exists()){
            log.delete();
        }
    }

    public void write(Robots[] rlist, Targets[] tlist, int time) throws IOException{

        FileWriter fw = new FileWriter(log, true);
        PrintWriter pw = new PrintWriter(fw);

        pw.format("TIME: %d%n", time);
        pw.println("ROBOTS COORDINATES");
        for(Robots each: rlist){
            pw.format("(%.2f, %.2f), (%.2f, %.2f)%n", each.Positions[0], each.Positions[1]
            , each.Velocity[0], each.Velocity[1]);
        }
        pw.println("DISCOVERED TARGETS");
        int flagged = 0;
        for(Targets each: tlist){
            if(each.flagged){
                pw.format("(%.2f, %.2f), (%.2f, %.2f)%n", each.Positions[0], each.Positions[1]
                , each.Velocity[0], each.Velocity[1]);
                flagged++;
            }
        }
        pw.println("TARGETS THAT ARE NOT DISCOVERED");
        for(Targets each: tlist){
            if(!each.flagged){
                pw.format("(%.2f, %.2f), (%.2f, %.2f)%n", each.Positions[0], each.Positions[1]
                        , each.Velocity[0], each.Velocity[1]);
            }
        }
        pw.format("NUMBER OF DETECTED TARGETS: %d%n%n", flagged);
        pw.close();

    }

}
