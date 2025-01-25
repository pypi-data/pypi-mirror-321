def get_epoch_containing_block(block: int, netuid: int, tempo: int = 360) -> range:
    """
    Reimplementing the logic from subtensor's Rust function:
        pub fn blocks_until_next_epoch(netuid: u16, tempo: u16, block_number: u64) -> u64
    See https://github.com/opentensor/subtensor.

    See also: https://github.com/opentensor/bittensor/pull/2168/commits/9e8745447394669c03d9445373920f251630b6b8

    If given block happens to be an end of an epoch, the resulting epoch will end with it. The beginning of an epoch
    is the first block when values like "dividends" are different (before an epoch they are constant for a full
    tempo).
    """
    assert tempo > 0

    interval = tempo + 1
    last_epoch = block - 1 - (block + netuid + 1) % interval
    next_tempo_block_start = last_epoch + interval
    return range(last_epoch, next_tempo_block_start)


def get_cycle_containing_block(block: int, netuid: int, tempo: int = 360) -> range:
    """
    A cycle contains two epochs, starts on an even one. A cycle is the basic unit of passage of time in compute horde,
    and validators testing miners are synchronised to cycles.
    """
    very_first_epoch = get_epoch_containing_block(0, netuid, tempo=tempo)
    epoch_containing_block = get_epoch_containing_block(block, netuid, tempo=tempo)

    if ((epoch_containing_block.start - very_first_epoch.start) / (tempo + 1)) % 2:
        # that's the second epoch in this cycle
        first_epoch = range(
            epoch_containing_block.start - (tempo + 1), epoch_containing_block.stop - (tempo + 1)
        )
        second_epoch = epoch_containing_block
    else:
        first_epoch = epoch_containing_block
        second_epoch = range(
            epoch_containing_block.start + (tempo + 1), epoch_containing_block.stop + (tempo + 1)
        )

    return range(first_epoch.start, second_epoch.stop)
