

/***************************************************************************
 *
 * 	FILE: 			Targets.java
 *
 * 	AUTHOR:			ROCKY LI
 *
 * 	DATE:			10/11/2017
 *
 * 	VER: 			1.0
 *
 * 	Purpose: 		Creates a Target
 *
 **************************************************************************/

public class Targets {

    public double[] Positions;
    public double[] Velocity;
    public double[] Acceleration;
    public Boolean flagged;
    public int id;

    // Mutator

    // Constructor

    public Targets(double[] pos, double[] vel, int id){
        Positions = pos;
        Velocity = vel;
        this.id = id;
        flagged = false;
    }

    public void Update(){

        Positions[0] += Velocity[0];
        Positions[1] += Velocity[1];

        if(OutOfBound(Positions, Arena.radius)){

            //Rebound from edge
            Positions[0] = Positions[0]*0.98;
            Positions[1] = Positions[1]*0.98;

            //Generate New Velocity
            Velocity = Arena.GenV();
        }

    }

    //Check if out of Bound

    public static Boolean OutOfBound(double[] pos, double radius){
        double dist = Math.sqrt(pos[1]*pos[1]+pos[0]*pos[0]);
        return dist > radius;
    }
}
