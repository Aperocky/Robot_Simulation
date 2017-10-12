import java.util.ArrayList;

/***************************************************************************
 *
 * 	FILE: 			MathFunc.java
 *
 * 	AUTHOR:			ROCKY LI
 *
 * 	DATE:			10/11/2017
 *
 * 	VER: 			1.0
 *
 * 	Purpose: 		Store useful math functions and tracking algorithms.
 *
 **************************************************************************/

public class Mathfunc {

    public static double CalcDist(double[] pos1, double[] pos2){
        double xdist = pos1[0] - pos2[0];
        double ydist = pos1[1] - pos2[1];
        return Math.sqrt(xdist*xdist + ydist*ydist);
    }

    // Calculating the force Vector of each target by location and distance.

    public static double[] TargetForceVector(double[] robot, double[] target){

        // Parameter Values
        double d1 = 4;
        double d2 = 8;
        double d3 = 30;
        double weight;

        double dist = CalcDist(target, robot);
        double xV = (target[0] - robot[0])/dist;
        double yV = (target[1] - robot[1])/dist;
        double[] unitVector = new double[]{xV, yV};
        if(dist < d2) {
            // Shortcut since d1 is half of d2 anyways.
            weight = 2/d2 * dist - 1;
        } else{
            // Shortcut since d3 = detection range anyways.
            weight = 1;
        }
        double[] forceVector = new double[2];
        forceVector[0] = unitVector[0]*weight;
        forceVector[1] = unitVector[1]*weight;

        return forceVector;
    }

    // Calculating the force Vector of each Robots by location and distance.

    public static double[] FriendlyForceVector(double[] self, double[] friend){

        //Parameter Values
        double dr1 = 12.5;
        double dr2 = 20;
        double weight = 0;

        double dist = CalcDist(self, friend);
        double xV = (friend[0] - self[0])/dist;
        double yV = (friend[1] - self[1])/dist;
        double[] unitVector = new double[]{xV, yV};
        if(dist<dr1){
            weight = -1;
        }
        else if (dist<dr2){
            weight = 1/(dr2-dr1)*(dist-dr1) - 1;
        }

        double[] forceVector = new double[2];
        forceVector[0] = unitVector[0]*weight;
        forceVector[1] = unitVector[1]*weight;

        return forceVector;
    }

    public static double[] TotalVector(ArrayList<double[]> forceVectors){
        double[] sumVectors = new double[2];
        for (double[] each: forceVectors){
            sumVectors[0] += each[0];
            sumVectors[1] += each[1];
        }
        return sumVectors;
    }

    public static double[] resizeVector(double[] vector, double value){
        double abs = Abs(vector);
        vector[0] = vector[0]/abs*value;
        vector[1] = vector[0]/abs*value;
        return vector;
    }

    public static double Abs(double[] vector){
        double sum = 0;
        for(double each: vector){
            sum += each*each;
        }
        return Math.sqrt(sum);
    }
}
