using System;
using System.Collections.Generic;

namespace DesignPatterns.Mediator
{
	public class CommandCentre : IAirportMediator
	{
		private List<Runway> _runways = new List<Runway>();
		private List<Aircraft> _aircrafts = new List<Aircraft>();

		public CommandCentre()
		{
		}

		public CommandCentre(Runway[] runways, Aircraft[] aircrafts)
		{
			foreach (var runway in runways)
			{
				RegisterRunway(runway);
			}

			foreach (var aircraft in aircrafts)
			{
				RegisterAircraft(aircraft);
			}
		}

		public void RegisterRunway(Runway runway)
		{
			_runways.Add(runway);
			runway.SetMediator(this);
		}

		public void RegisterAircraft(Aircraft aircraft)
		{
			_aircrafts.Add(aircraft);
			aircraft.SetMediator(this);
		}

		public bool RequestLanding(Aircraft aircraft)
		{
			Console.WriteLine($"Літак {aircraft.Name} запитує дозвіл на посадку.");
			Console.WriteLine("Перевіряємо наявність вільної злітної смуги.");

			var availableRunway = GetAvailableRunway();
			if (availableRunway != null)
			{
				Console.WriteLine($"Літак {aircraft.Name} здійснив посадку.");
				availableRunway.SetBusy(aircraft);
				return true;
			}
			else
			{
				Console.WriteLine("Неможливо здійснити посадку, всі злітні смуги зайняті.");
				return false;
			}
		}


		public void NotifyTakeOff(Aircraft aircraft)
		{
			Console.WriteLine($"Літак {aircraft.Name} вилітає.");

			foreach (var runway in _runways)
			{
				if (runway.IsBusyWithAircraftId == aircraft.Id)
				{
					runway.SetFree();
					Console.WriteLine($"Літак {aircraft.Name} вилетів.");
					return;
				}
			}
		}

		public Runway GetAvailableRunway()
		{
			foreach (var runway in _runways)
			{
				if (!runway.IsBusy())
				{
					return runway;
				}
			}
			return null;
		}
	}
}