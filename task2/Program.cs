using System;

namespace DesignPatterns.Mediator
{
    class Program
    {
        static void Main(string[] args)
        {
            CommandCentre commandCentre = new CommandCentre();

            Runway runway1 = new Runway();
            Runway runway2 = new Runway();

            commandCentre.RegisterRunway(runway1);
            commandCentre.RegisterRunway(runway2);

            Aircraft aircraft1 = new Aircraft("Boeing 747", 300);
            Aircraft aircraft2 = new Aircraft("Airbus A320", 180);
            Aircraft aircraft3 = new Aircraft("Cessna 172", 4);

            commandCentre.RegisterAircraft(aircraft1);
            commandCentre.RegisterAircraft(aircraft2);
            commandCentre.RegisterAircraft(aircraft3);

            aircraft1.Land();
            aircraft2.Land();
            aircraft3.Land(); 

            aircraft1.TakeOff();
            aircraft3.Land(); 

            Console.ReadLine();
        }
    }
}