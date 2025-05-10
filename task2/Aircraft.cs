using System;

namespace DesignPatterns.Mediator
{
	public class Aircraft
	{
		public readonly Guid Id = Guid.NewGuid();
		public string Name;
		public int Size;
		private IAirportMediator _mediator;
		public bool IsTakingOff { get; private set; }

		public Aircraft(string name, int size)
		{
			this.Name = name;
			this.Size = size;
		}

		public void SetMediator(IAirportMediator mediator)
		{
			_mediator = mediator;
		}

		public void Land()
		{
			if (_mediator.RequestLanding(this))
			{
				IsTakingOff = false;
			}
		}

		public void TakeOff()
		{
			IsTakingOff = true;
			_mediator.NotifyTakeOff(this);
			IsTakingOff = false;
		}
	}
}