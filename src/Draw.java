import javax.swing.*;
import java.awt.*;

/***************************************************************************
 *
 * 	FILE: 			Draw.java
 *
 * 	AUTHOR:			ROCKY LI
 *
 * 	DATE:			10/11/2017
 *
 * 	VER: 			1.0
 *
 * 	Purpose: 		Draw the robots and targets to a 2D graph
 *
 **************************************************************************/

public class Draw extends JFrame{

    public Robots[] robotlist;
    public Targets[] targetlist;

    public Draw(Robots[] robot, Targets[] target){
        this.setPreferredSize(new Dimension(500, 500));
        this.pack();
        this.setVisible(true);
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        this.robotlist = robot;
        this.targetlist = target;
    }

    public void paintComponent(Graphics g) throws InterruptedException{
        super.paintComponents(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setColor(Color.blue);
    }
}
