using System;

namespace DesignPatterns.Mediator
{
	public class Runway
	{
		public readonly Guid Id = Guid.NewGuid();
		public Guid? IsBusyWithAircraftId;
		private IAirportMediator _mediator;

		public void SetMediator(IAirportMediator mediator)
		{
			_mediator = mediator;
		}

		public bool IsBusy()
		{
			return IsBusyWithAircraftId.HasValue;
		}

		public void SetBusy(Aircraft aircraft)
		{
			IsBusyWithAircraftId = aircraft.Id;
			HighLightRed();
		}

		public void SetFree()
		{
			IsBusyWithAircraftId = null;
			HighLightGreen();
		}

		public void HighLightRed()
		{
			Console.WriteLine($"«л≥тна смуга {this.Id} зайн€та!");
		}

		public void HighLightGreen()
		{
			Console.WriteLine($"«л≥тна смуга {this.Id} в≥льна!");
		}
	}
}