import java.util.ArrayList;

/***************************************************************************
 *
 * 	FILE: 			Robots.java
 *
 * 	AUTHOR:			ROCKY LI
 *
 * 	DATE:			10/11/2017
 *
 * 	VER: 			1.0
 *
 * 	Purpose: 		Creates a Robot object.
 *
 **************************************************************************/

public class Robots {

    public double[] Positions;
    public double[] Velocity;
    public double[] Acceleration;
    public int id;
    public double drange;

    // A real time update of the targets being detected.
    private ArrayList<Targets> detected;

    // A real time update of teammate information.
    private ArrayList<Robots> teaminfo;

    // Mutator

    public void ChangeV(double[] velocity){
        this.Velocity = velocity;
    }

    public void Detect(ArrayList<Targets> detected){
        this.detected = detected;
    }

    public void Communicate(ArrayList<Robots> teaminfo){
        this.teaminfo = teaminfo;
    }

    // Init

    public Robots(double[] pos, double[] vel, double drange, int id){
        Positions = pos;
        Velocity = vel;
        this.drange = drange;
        this.id = id;
    }

    public void Update(){
        Positions[0] += Velocity[0];
        Positions[1] += Velocity[1];
        if(Targets.OutOfBound(Positions, Arena.radius)) {
            //Rebound from edge
            Positions[0] = Positions[0] * 0.98;
            Positions[1] = Positions[1] * 0.98;
        }
    }

    // Flag Targets if in range

    public Boolean flag(double[] pos){
        double dist = Mathfunc.CalcDist(pos, this.Positions);
        return dist < drange;
    }

    // The onboard computer make decision about velocity

    public void CalcV(){

        // Initiate a force vector array.
        ArrayList<double[]> ForceVectors = new ArrayList<double[]>();
        for(Targets enemy: detected){
            ForceVectors.add(Mathfunc.TargetForceVector(this.Positions, enemy.Positions));
        }
        for(Robots friend: teaminfo){
            if(friend == this){
                continue;
            }
            ForceVectors.add(Mathfunc.FriendlyForceVector(this.Positions, friend.Positions));
        }

        //Get the sum of the array
        double[] TotalVector = Mathfunc.TotalVector(ForceVectors);

        double Gear = 2;
        //Important, this make robots faster when not enough targets are around. Crank up the GEARS!
        TotalVector[0] *= Gear;
        TotalVector[1] *= Gear;

        if(Mathfunc.Abs(TotalVector) > 2){
            TotalVector = Mathfunc.resizeVector(TotalVector, 2);
        }
        this.ChangeV(TotalVector);
    }

}
