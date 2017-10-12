

/***************************************************************************
 *
 * 	FILE: 			Arena.java
 *
 * 	AUTHOR:			ROCKY LI
 *
 * 	DATE:			10/11/2017
 *
 * 	VER: 			1.0
 *
 * 	Purpose: 		Creates an Arena with targets moving around
 *
 **************************************************************************/

public class Arena {

    public static double radius;
    public int TargetCount;
    public int RobotCount;
    public Robots[] robotlist;
    public Targets[] targetlist;

    // Generate random velocity

    public static double[] GenV(){

        double direction = 2*Math.PI*Math.random();
        double Vx = Math.cos(direction)*1.5;
        double Vy = Math.sin(direction)*1.5;
        return new double[]{Vx, Vy};

    }

    // Generate random positions

    public static double[] GenLocation(){

        double direction = 2*Math.PI*Math.random();
        // Explaination: Since the inner space is smaller, we'll twitch the distance to make the distribution even.
        double distance = Math.sqrt(10000*Math.random());
        double Xpos = Math.cos(direction)*distance;
        double Ypos = Math.sin(direction)*distance;
        return new double[]{Xpos, Ypos};

    }

    // Initialize the ARENA FOR BATTLE!

    public Arena(int m, int n, double radius){

        robotlist = new Robots[m];
        targetlist = new Targets[n];

        for(int i = 0; i<m; i++){
            double[] pos = GenLocation();
            double[] vel = GenV();
            robotlist[i] = new Robots(pos, vel, 30, i);
        }

        for(int j = 0; j<n; j++){
            double[] pos = GenLocation();
            double[] vel = GenV();
            targetlist[j] = new Targets(pos, vel, j);
        }
    }

}
