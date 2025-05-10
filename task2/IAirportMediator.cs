using System;

namespace DesignPatterns.Mediator
{
	public interface IAirportMediator
	{
		void RegisterRunway(Runway runway);
		void RegisterAircraft(Aircraft aircraft);
		bool RequestLanding(Aircraft aircraft);
		void NotifyTakeOff(Aircraft aircraft);
		Runway GetAvailableRunway();
	}
}